const ffi = require("ffi-napi");
const ref = require("ref-napi");

const libPath = "./rust-digest/target/debug/libdigest"

const libDigest = ffi.Library(libPath, {
    "digest": ["string", ["string"]],
});

const { digest } = libDigest;

console.log("Hello World SHA256: ", digest("Hello World"));