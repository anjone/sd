/* tslint:disable */
/**
* @param {string} data 
* @returns {string} 
*/
export function digest(data: string): string;
/**
* @param {string} data 
* @param {string} elem_id 
*/
export function digest_attach(data: string, elem_id: string): void;
/**
*/
export function start(): void;

/**
* If `module_or_path` is {RequestInfo}, makes a request and
* for everything else, calls `WebAssembly.instantiate` directly.
*
* @param {RequestInfo | BufferSource | WebAssembly.Module} module_or_path
*
* @returns {Promise<any>}
*/
export default function init (module_or_path?: RequestInfo | BufferSource | WebAssembly.Module): Promise<any>;
        