use std::os::raw::{c_char, c_short};
use std::ffi::CString;

#[link(name="ncurses")]
extern {
    fn initscr();
    fn printw(fmt: *const c_char, ...);
    fn refresh();
    fn getch();
    fn endwin();
    fn start_color();
    fn init_pair(pair:c_short, f:c_short, b:c_short);
    fn attron(pair:c_short);
    fn COLOR_PAIR(pair: c_short) -> c_short;
}

struct Ncurses;

impl Ncurses {
     fn init_screen() {
         unsafe { initscr(); start_color(); }
     }

     fn refresh() {
         unsafe { refresh(); }
     }

     fn get_char() {
         unsafe { getch(); }
     }

     fn deinit_screen() {
         unsafe { endwin(); }
     }

     fn color_red() {
         unsafe { init_pair(1, 1, 0); attron(COLOR_PAIR(1)); }
     }
}

fn main() {
    let the_message = CString::new("Rust and ncurses working together, and here is a number: %d").unwrap();
    Ncurses::init_screen();
    Ncurses::color_red();
    unsafe {
        printw(the_message.as_ptr(), 1);
    }
    Ncurses::refresh();
    Ncurses::get_char();
    Ncurses::deinit_screen();
}