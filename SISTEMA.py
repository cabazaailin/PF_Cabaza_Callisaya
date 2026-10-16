"""Sistema de gestion de transporte universitario - PFU-111"""


class Vehiculo:
    

    def __init__(self, codigo, marca, capacidad, kilometraje):
        self._codigo = codigo
        self._marca = marca
        self.capacidad = capacidad        # usa el setter (valida)
        self.kilometraje = kilometraje    # usa el setter (valida)


    @property
    def codigo(self):
        return self._codigo

    @property
    def marca(self):
        return self._marca

    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, valor):
        if valor < 0:
            raise ValueError("La capacidad no puede ser negativa.")
        self._capacidad = valor

    @property
    def kilometraje(self):
        return self._kilometraje

    @kilometraje.setter
    def kilometraje(self, valor):
        if valor < 0:
            raise ValueError("El kilometraje no puede ser negativo.")
        self._kilometraje = valor

    def mostrar_info(self):
        return (f"Codigo: {self._codigo} | Marca: {self._marca} | "
                f"Capacidad: {self._capacidad} | Km: {self._kilometraje}")

    def calcular_costo_operativo(self):
        raise NotImplementedError("Cada vehiculo debe calcular su costo.")


def _validar_costo(valor):
    if valor <= 0:
        raise ValueError("El costo por kilometro debe ser mayor a 0.")
    return valor


class Trufi(Vehiculo):
    def __init__(self, codigo, marca, capacidad, kilometraje, rutas, costo_km):
        super().__init__(codigo, marca, capacidad, kilometraje)
        if rutas < 0:
            raise ValueError("Las rutas no pueden ser negativas.")
        self._rutas = rutas
        self._costo_km = _validar_costo(costo_km)

    def mostrar_info(self):
        return (f"[Trufi]     {super().mostrar_info()} | "
                f"Rutas: {self._rutas} | Costo/km: {self._costo_km}")

    def calcular_costo_operativo(self):
        return self.kilometraje * self._costo_km


class Minibus(Vehiculo):
    def __init__(self, codigo, marca, capacidad, kilometraje, viajes, costo_km):
        super().__init__(codigo, marca, capacidad, kilometraje)
        if viajes < 0:
            raise ValueError("Los viajes no pueden ser negativos.")
        self._viajes = viajes
        self._costo_km = _validar_costo(costo_km)

    def mostrar_info(self):
        return (f"[Minibus]   {super().mostrar_info()} | "
                f"Viajes: {self._viajes} | Costo/km: {self._costo_km}")

    def calcular_costo_operativo(self):
        return self.kilometraje * self._costo_km


class Radiotaxi(Vehiculo):
    def __init__(self, codigo, marca, capacidad, kilometraje, area, costo_km):
        super().__init__(codigo, marca, capacidad, kilometraje)
        self._area = area
        self._costo_km = _validar_costo(costo_km)

    def mostrar_info(self):
        return (f"[Radiotaxi] {super().mostrar_info()} | "
                f"Area: {self._area} | Costo/km: {self._costo_km}")

    def calcular_costo_operativo(self):
        return self.kilometraje * self._costo_km



def pedir_numero(texto, tipo=float):
    while True:
        try:
            return tipo(input(texto))
        except ValueError:
            print("  Dato invalido, escribe un numero.")


def registrar(flota, clase, extra_texto, extra_tipo):
    print(f"\n--- Registrar {clase.__name__} ---")
    try:
        codigo = input("Codigo: ")
        marca = input("Marca: ")
        capacidad = pedir_numero("Capacidad de pasajeros: ", int)
        km = pedir_numero("Kilometraje recorrido: ")
        extra = (pedir_numero(extra_texto, extra_tipo)
                 if extra_tipo else input(extra_texto))
        costo = pedir_numero("Costo por kilometro (Bs): ")
        flota.append(clase(codigo, marca, capacidad, km, extra, costo))
        print("Vehiculo registrado correctamente.")
    except ValueError as error:
        print(f"Error: {error}  (no se registro)")


def mostrar(flota):
    if not flota:
        print("No hay vehiculos registrados.")
    for v in flota:
        print(v.mostrar_info())


def costos(flota):
    for v in flota:   
        print(f"{v.codigo}: Bs {v.calcular_costo_operativo():.2f}")


def total(flota):
    suma = sum(v.calcular_costo_operativo() for v in flota)
    print(f"Costo operativo total: Bs {suma:.2f}")


def menu():
    flota = []   
    while True:
        print("\n===== TRANSPORTE UNIVERSITARIO =====")
        print("1. Registrar trufi\n2. Registrar minibus\n3. Registrar radiotaxi")
        print("4. Mostrar vehiculos\n5. Costo de cada vehiculo")
        print("6. Costo total\n7. Salir")
        op = input("Opcion: ")
        if op == "1":
            registrar(flota, Trufi, "Numero de rutas: ", int)
        elif op == "2":
            registrar(flota, Minibus, "Numero de viajes: ", int)
        elif op == "3":
            registrar(flota, Radiotaxi, "Area asignada: ", None)
        elif op == "4":
            mostrar(flota)
        elif op == "5":
            costos(flota)
        elif op == "6":
            total(flota)
        elif op == "7":
            print("Hasta luego.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()