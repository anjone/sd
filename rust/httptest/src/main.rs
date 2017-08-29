extern crate hyper;
extern crate tokio_core;

use hyper::StatusCode;
use hyper::Client;
use tokio_core::reactor::Core;

use std::io::{self, Write};
use std::collections::HashMap;

macro_rules! http_test {
    ($url:tt GET => $code:expr) => {
        let mut core = Core::new().unwrap();
        let client = Client::new(&core.handle());
        let uri = $url.parse().unwrap();
        let work = client.get(uri);
        let res = core.run(work).unwrap();
        println!("GET {} => {}", $url, $code);
        assert_eq!(res.status(), $code);
    };
    /*($url:tt POST => $code:expr) => {
        let mut core = Core::new().unwrap();
        let client = Client::new(&core.handle());
        let work = client.post($url);
        let res = core.run(work).unwrap();
        println!("POST {} => {}", $url, $code);
        assert_eq!(res.status(), $code);
    };*/
}

macro_rules! html_list {

    //($($x:tt,)*) => { stringify!(<ul>$(<li>$x</li>)*) };
    //($($x:tt),*) => { stringify!(<ul>$(<li>$x</li>)*) };

    ($($x: expr,)*) => {
        stringify!(<ul>$(<li>$x</li>)*</ul>)
    };
    ($($x: expr),*) => {
        stringify!(<ul>$(<li>$x</li>)*</ul>)
    };
}

macro_rules! seq_gen {
    ($($x:expr,)*) => {vec![$($x,)*]};
    ($($x:expr),*) => {vec![$($x),*]};
    ($($k:expr => $v:expr;)*) => {
        {
            let mut h = HashMap::new();
            $(
                h.insert($k, $v);
            )*
            h
        }
    };
    ($($k:expr => $v:expr);*) => {
        {
            let mut h = HashMap::new();
            $(
                h.insert($k, $v);
            )*
            h
        }
    };
}

fn main() {
    println!("Hello, world!");
    http_test!("http://10.228.64.47" GET => StatusCode::Ok);
    //http_test!("http://www.126.com" POST => StatusCode::MethodNotAllowed);
    //http_test!("http://www.126.com" POST => StatusCode::Ok);

    println!(html_list![1,2,3]);

    println!("{:?}", seq_gen!(1,2,3,));
    println!("{:?}", seq_gen!('a'=>2;'b'=>4;));
}
