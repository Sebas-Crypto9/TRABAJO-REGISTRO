import 'dart:io';

void main() {
  print("=== SE LE PIDE AL USUARIO ENGRESAR SUS DATOS PERSONALES ===");

  stdout.write("Primer Nombre: ");
  String nom1 = stdin.readLineSync() ?? '';

  stdout.write("Segundo Nombre: ");
  String nom2 = stdin.readLineSync() ?? '';

  stdout.write("Primer Aprellido: ");
  String ape1 = stdin.readLineSync() ?? '';

  stdout.write("Segundo Nombre: ");
  String ape2 = stdin.readLineSync() ?? '';
}
