package org.std.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.std.domain.Journal;

/**
 * Created by jiangqizhou-001 on 2017/4/28 0028.
 */
public interface JournalRepository extends JpaRepository<Journal, Long> {
}
