use std::error::Error;
use std::fmt;

#[derive(PartialEq, Debug, Clone)]
enum TerrainGround {
    Soil,
    Stone,
}

#[derive(PartialEq, Debug, Clone)]
enum TerrainBlock {
    Tree,
    Soil,
    Stone,
}

#[derive(PartialEq, Debug, Clone)]
enum Being {
    Orc,
    Human,
}

#[derive(Debug, Clone)]
struct Square {
    ground: TerrainGround,
    block: Option<TerrainBlock>,
    being: Option<Being>,
}

#[derive(Debug)]
struct Grid {
    size: (usize, usize),
    squares: Vec<Square>,
}

enum Direction {
    West,
    East,
    North,
    South
}

#[derive(PartialEq, Debug)]
enum MovementError {
    NoBeingInSquare,
    FellOffTheGrid,
    AnotherBeingInSquare,
    MovedToBadTerrain,
}

impl fmt::Display for MovementError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "MovementError!")
    }
} 

impl Error for MovementError {
    fn description(&self) -> &str {
        match self {
            NoBeingInSquare => "No being in square",
            FellOffTheGrid => "Tried to move off the grid",
            AnotherBeingInSquare => "Tried to move on another being",
            MovedToBadTerrain => "Tried to move to inaccessible terrain",
        }
    }

    fn cause(&self) -> Option<&Error> {
        None
    }
}

impl Grid {

    fn move_being_in_coord(&mut self, coord: (usize, usize), dir: Direction) -> Result<(usize, usize), MovementError> {
        let copy_of_squares = self.squares.clone();
        let square = copy_of_squares.get(coord.0*self.size.0 + coord.1).expect("Index out of bounds trying to get being");
        /*match square.beings {
            Some(_) => Ok((0,0)),
            None => Err(MovementError::NoBeingInSquare),
        }*/
        if square.being == None {
            return Err(::MovementError::NoBeingInSquare);
        }

        let new_coord = match dir {
            Direction::North => (coord.0 - 1, coord.1),
            Direction::East  => (coord.0, coord.1 + 1),
            Direction::South => (coord.0 + 1, coord.1),
            Direction::West  => (coord.0, coord.0 - 1),
        };

        if new_coord.0 >= self.size.0 || new_coord.1 >= self.size.1 {
            return Err(::MovementError::FellOffTheGrid);
        }

        let new_square = copy_of_squares.get(new_coord.0 * self.size.0 + new_coord.1).unwrap();
        if new_square.being != None {
            return Err(::MovementError::AnotherBeingInSquare);
        }
        if new_square.ground == TerrainGround::Stone {
            return Err(::MovementError::MovedToBadTerrain);
        }

        self.squares[new_coord.0 * self.size.0 + new_coord.1] = Square {
            ground: new_square.ground.clone(),
            block: new_square.block.clone(),
            being: square.being.clone(),
        };
        self.squares[coord.0 * self.size.0 + coord.1] = Square {
            ground: square.ground.clone(),
            block: square.block.clone(),
            being: None,
        };

        Ok(new_coord)
    }

    fn generate_empty(size_x: usize, size_y: usize) -> Grid {
         let number_of_squares = size_x * size_y;
         let mut squares: Vec<Square> = Vec::with_capacity(number_of_squares);
         for _ in 0..number_of_squares {
             squares.push(Square{ground: TerrainGround::Soil, block: None, being: None});
         }
         Grid {
            size: (size_x, size_y),
            squares: squares
         }
     }
}

#[cfg(test)]
mod tests {
     #[test]
     fn test_empty_grid() {
         let grid = ::Grid::generate_empty(5, 13);
         assert_eq!(grid.size, (5, 13));
         let mut number_of_squares = 0;
         for square in &grid.squares {
             assert_eq!(square.ground, ::TerrainGround::Soil);
             assert_eq!(square.block, None);
             assert_eq!(square.being, None);
             number_of_squares += 1;
         }
         assert_eq!(grid.squares.len(), 5*13);
         assert_eq!(number_of_squares, 5*13);
     }
     #[test]
     fn test_move_being_without_being_in_square() {
         let mut grid = ::Grid::generate_empty(3, 3);
         assert_eq!(grid.move_being_in_coord((0, 0), ::Direction::West), Err(::MovementError::NoBeingInSquare));
     }

     #[test]
     fn test_move_being_off_the_grid() {
         let mut grid = ::Grid::generate_empty(3, 3);
         let human = ::Being::Human;

         grid.squares[3 * 3 - 1].being = Some(human);
         assert_eq!(grid.move_being_in_coord((2, 2), ::Direction::East), Err(::MovementError::FellOffTheGrid));
     }

     #[test]
     fn test_move_being_on_another_being() {
         let mut grid = ::Grid::generate_empty(3, 3);
         let human = ::Being::Human;
         let orc = ::Being::Orc;

         grid.squares[0].being = Some(human);
         grid.squares[1].being = Some(orc);
         assert_eq!(grid.move_being_in_coord((0, 0), ::Direction::East), Err(::MovementError::AnotherBeingInSquare));
     }

     #[test]
     fn test_move_being_on_stone() {
         let mut grid = ::Grid::generate_empty(3, 3);
         let human = ::Being::Human;
         let stone = ::TerrainGround::Stone;

         grid.squares[0].being = Some(human);
         grid.squares[1].ground = stone;
         assert_eq!(grid.move_being_in_coord((0, 0), ::Direction::East), Err(::MovementError::MovedToBadTerrain));
     }

     #[test]
     fn test_move_successfully() {
         let mut grid = ::Grid::generate_empty(3, 3);
         let human = ::Being::Human;

         grid.squares[0].being = Some(human);
         assert_eq!(grid.move_being_in_coord((0, 0), ::Direction::South), Ok((1, 0)));
         assert_eq!(grid.squares[0].being, None);
         assert!(grid.squares[3].being != None);
     }
}

fn main() {
    println!("Hello, world!");
}
