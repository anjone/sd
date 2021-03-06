use diesel::result::Error;
use diesel;
use diesel::sqlite::SqliteConnection;
use super::models::*;
use diesel::prelude::*;
use super::schema::posts;

pub fn get_post(conn: &SqliteConnection, id: i32) -> Result<Post, Error> {
    posts::table.find(id).first::<Post>(conn)
}

pub fn get_posts(conn: &SqliteConnection) -> Result<Vec<Post>, Error> {
    posts::table.load::<Post>(conn)
}

pub fn create_post(conn: &SqliteConnection, post: PostData) -> bool {
    diesel::insert(&post).into(posts::table).execute(conn).is_ok()
}

pub fn delete_post(conn: &SqliteConnection, id: i32) -> Result<usize, Error> {
    diesel::delete(posts::table.find(id)).execute(conn)
}

pub fn update_post(conn: &SqliteConnection, id: i32, update_post: PostData) -> bool {
    diesel::update(posts::table.find(id)).set(&update_post).execute(conn).is_ok()
}