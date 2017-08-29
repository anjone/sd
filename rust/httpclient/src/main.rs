extern crate hyper;
extern crate tokio_core;
extern crate futures;
extern crate pretty_env_logger;

use std::io::{self, Write};
use std::str;
use futures::{Future, Stream};
use hyper::{Client, Method, Request};
use hyper::header::{ContentLength, ContentType};
use tokio_core::reactor::Core;


fn run() -> Result<(), Box<::std::error::Error>> {
    let mut core = Core::new()?;
    let client = Client::new(&core.handle());
    let getUri = "http://10.228.64.47".parse()?;
    //let work = client.get(uri);
    let get = client.get(getUri).and_then(|res| {
        println!("Response: {}", res.status());
        /*res.body().for_each(|chunk| {
            io::stdout().write_all(&chunk).map(|_| ()).map_err(From::from)
        })*/
        res.body().concat2()
    });

    let postUri = "http://10.228.64.47".parse()?;
    let req = Request::new(Method::Post, postUri);
    let post = client.request(req).and_then(|res| {
        println!("POST: {}", res.status());
        res.body().concat2()
    });

    let work = post.join(get);

    let (posted, got) = core.run(work).unwrap();

    println!("POST: {}", str::from_utf8(&posted)?);
    println!("GET: {}", str::from_utf8(&got)?);

    Ok(())
}

fn main() {
    println!("Hello, world!");
    run();

    /*pretty_env_logger::init().unwrap();

    let mut core = Core::new().unwrap();
    let client = Client::new(&core.handle());
    let uri = "http://10.228.64.47".parse().unwrap();

    let work = client.get(uri).and_then(|res| {
        println!("Response: {}", res.status());
        println!("Headers: \n{}", res.headers());

        res.body().for_each(|chunk| {
            io::stdout().write_all(&chunk).map_err(From::from)
        })
    }).map(|_| {
        println!("\nDone!");
    });

    core.run(work).unwrap();*/
}
