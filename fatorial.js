function factorial (num){
  let fac = 1;
  for(let i = num; i>1; i--){
    num *= i;
  }
  return num;
}
