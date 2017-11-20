#![crate_type = "staticlib"]

#[no_mangle]
pub extern fn double_input(input: i32) -> i32 {
    // add code here
    input * 2
}