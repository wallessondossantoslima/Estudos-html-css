function myFunction() {
  let str = document.getElementById("text");
  if (str.value == "") {
    str.focus();
    return;
  }
  let c = "ASCII Code: ";
  document.getElementById("char").innerHTML = c + str.value.charCodeAt(0);
}
