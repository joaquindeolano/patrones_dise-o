class ApprovalHandler:
    def __init__(self, successor=None):
        self._successor = successor

    def set_successor(self, successor):
        self._successor = successor

    def process_document(self, document):
        if self._successor:
            self._successor.process_document(document)

class ApprovalHandler_A(ApprovalHandler):
    def process_document(self, document):
        if document == "Document1":
            print("Ha sido aprobado el documento 1 por: 'A'") 
        else:
            super().process_document(document)

class ApprovalHandler_B(ApprovalHandler):
    def process_document(self, document):
        if document == "Document2":
            print("Ha sido aprobado el documento 2 por: 'B'")
        else:
            super().process_document(document)

class ApprovalHandler_C(ApprovalHandler):
    def process_document(self, document):
        if document == "Document3":
            print("Ha sido aprobado el documento 3 por: 'C'")
        else:
            print("El documento ha sido denegado")