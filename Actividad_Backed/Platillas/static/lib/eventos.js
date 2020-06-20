document.addEventListener("mousedown",iniciarDibujo);
document.addEventListener("mousemove",dibujando);
document.addEventListener("mouseup",parar);

var cuadrito = document.getElementById("area_de_dibujo");
var papel = cuadrito.getContext("2d");
var limites = cuadrito.width;
var dibujo = false;
var xi,yi,xf,yf;

contorno();

function iniciarDibujo(evento){
  dibujo = true;
}

function parar(evento){
  dibujo = false;
}

function dibujando(evento){
  xf = evento.offsetX;
  yf = evento.offsetY;
  colorcito = "Blue"

  if (dibujo == true) {
    dibujarLinea(colorcito ,xi ,yi , xf, yf , papel);
  }

  xi = xf;
  yi = yf;

}

function contorno() {
  dibujarLinea("black",1 , 1, 1, limites - 1, papel);
  dibujarLinea("black",1 , limites - 1, limites - 1, limites - 1, papel);
  dibujarLinea("black",limites - 1 , 1, limites - 1, limites - 1, papel);
  dibujarLinea("black",limites - 1 , 1, 1, 1, papel);
}

function dibujarLinea(color, xin, yin, xfi, yfi, lienzo) {
  lienzo.beginPath();
  lienzo.strokeStyle = color;
  lienzo.lineWidth = 3;
  lienzo.moveTo(xin, yin);
  lienzo.lineTo(xfi, yfi);
  lienzo.stroke();
  lienzo.closePath();
}
