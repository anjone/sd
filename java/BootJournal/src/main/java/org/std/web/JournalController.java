package org.std.web;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;
import org.std.repository.JournalRepository;

/**
 * Created by jiangqizhou-001 on 2017/4/28 0028.
 */
//@RestController
public class JournalController {

    private static final String VIEW_INDEX = "index";

    @Autowired
    private JournalRepository journalRepository;

    @RequestMapping(value="/", method = RequestMethod.GET)
    public ModelAndView index(ModelAndView modelAndView){
        modelAndView.setViewName(VIEW_INDEX);
        modelAndView.addObject("journal", journalRepository.findAll());
        return modelAndView;
    }

}
