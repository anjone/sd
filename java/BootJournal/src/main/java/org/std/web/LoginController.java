package org.std.web;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

/**
 * Created by jiangqizhou-001 on 2017/4/28 0028.
 */
//@Controller
public class LoginController {

    private static final String VIEW_LOGIN = "login";

    @RequestMapping(value="/login")
    public ModelAndView login(ModelAndView modelAndView){
        modelAndView.setViewName(VIEW_LOGIN);
        return modelAndView;
    }

}
