import { Component, OnInit, AfterViewInit, ViewChild } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator} from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { FormControl } from '@angular/forms';
import { OptionalTextValidation } from 'src/app/common/validations';
import { UserService } from 'src/app/user/user/user.service';
import { merge, of, from } from 'rxjs';
import { debounceTime, startWith, switchMap, catchError, map } from 'rxjs/operators';
import { IUser } from 'src/app/user/user/user';

@Component({
  selector: 'app-user-table',
  templateUrl: './user-table.component.html',
  styleUrls: ['./user-table.component.scss']
})
export class UserTableComponent implements OnInit, AfterViewInit {
  displayedColumns = ['name', 'email', 'role', 'status', 'id'];
  dataSource = new MatTableDataSource();
  resultsLength = 0;
  _isLoadingResults = true;
  _hasError = false;
  errorText = '';
  _skipLoading = false;

  search = new FormControl('', OptionalTextValidation);

  @ViewChild(MatPaginator, { static: false }) paginator: MatPaginator;
  @ViewChild(MatSort, { static: false }) sort: MatSort;

  ngAfterViewInit(): void {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;

    this.sort.sortChange.subscribe(() => (this.paginator.pageIndex = 0));

    if (this._skipLoading) {
      return;
    }

    merge(
      this.sort.sortChange,
      this.paginator.page,
      this.search.valueChanges.pipe(debounceTime(1000))
    ).pipe(
      startWith({}),
      switchMap(() => {
        this._isLoadingResults = true;
        return this.userService.getUsers(
          this.paginator.pageSize,
          this.search.value,
          this.paginator.pageIndex,
        );
      }),
      map((data: { total: number, items: IUser[] }) => {
        this._isLoadingResults = false;
        this._hasError = false;
        this.resultsLength = data.total;

        return data.items;
      }),
      catchError(err => {
        this._isLoadingResults = false;
        this._hasError = true;
        this.errorText = err;
        return of([]);
      })
    ).subscribe(data => (this.dataSource.data = data));
  }

  get isLoadingResults() {
    return this._isLoadingResults;
  }

  get hasError() {
    return this._hasError;
  }

  constructor(private userService: UserService) { }

  ngOnInit() {
  }

}
