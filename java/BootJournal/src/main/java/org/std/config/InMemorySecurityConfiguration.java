package org.std.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.authentication.configuration.EnableGlobalAuthentication;

/**
 * Created by jiangqizhou-001 on 2017/4/28 0028.
 */
//@Configuration
//@EnableGlobalAuthentication
public class InMemorySecurityConfiguration {

    @Autowired
    public void configureGlobal(AuthenticationManagerBuilder auth) throws Exception {
        auth.inMemoryAuthentication().withUser("spring").password("boot").roles("USER")
                .and().withUser("admin").password("password").roles("USER", "ADMIN");
    }

}
