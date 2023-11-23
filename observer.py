"""
Este patrón es útil cuando un objeto necesita notificar a otros objetos sobre cambios en su estado. Implementa un sistema de notificación donde, cuando un objeto cambia, notifica automáticamente a sus observadores.
"""

class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)
    
    def notify_observer(self, message):
        for observer in self._observers:
            observer.notify(message)

class Observer:
    def notify(self, message):
        print("Notificado con:", message)

subject = Subject()
observer1 = Observer()
observer2 = Observer()
subject.register_observer(observer1)
subject.register_observer(observer2)
subject.notify_observer("Cambio de estado")
