#[macro_use]
extern crate cpython;

use cpython::{Python, PyResult};

fn fibo(_py: Python, n: u64) -> PyResult<u64> {
    if n < 2 {
        return Ok(1)
    }

    let mut pre1 = 1;
    let mut pre2 = 1;
    for _ in 1..n {
        let new = pre1 + pre2;
        pre1 = pre2;
        pre2 = new;
    }
    Ok(pre1)
}

py_module_initializer!(prlib, initprlib, PyInit_prlib, |py, m| {
    try!(m.add(py, "fibo", py_fn!(py, fibo(rand_int: u64))));
    Ok(())
});

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
