package org.std.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.std.domain.Journal;
import org.std.repository.JournalRepository;

import java.text.ParseException;
import java.util.List;

/**
 * Created by jiangqizhou-001 on 2017/4/28 0028.
 */
@Service
public class JournalService {

    private static final Logger log = LoggerFactory.getLogger(JournalService.class);

    @Autowired
    private JournalRepository journalRepository;

    public List<Journal> findAll() {
        return journalRepository.findAll();
    }

    public void insertData() throws ParseException {
        log.info("> Inserting data ...");
        journalRepository.save(new Journal("Get to know Spring Boot","Today I will learn Spring Boot","01/01/2016"));
        journalRepository.save(new Journal("Simple Spring Boot Project","I will do my first Spring Boot Project","01/02/2016"));
        journalRepository.save(new Journal("Spring Boot Reading","Read more about Spring Boot","02/01/2016"));
        journalRepository.save(new Journal("Spring Boot in the Cloud","Spring Boot using Cloud Foundry","03/01/2016"));
        log.info("> Done.");
    }

}
