/**
 * @param {number} a
 * @param {number} b
 *
 * @returns {number}
 */
function solve(a, b) {
	x = '';
  	if(a > b){
    	x = '>' 
    }else if(a == b){
    	x = '=';
    }else{
    	x = '<';
    }
    return x;
}