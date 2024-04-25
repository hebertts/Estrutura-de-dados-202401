import tkinter as tk
from tkinter import simpledialog, messagebox
from ttkthemes import ThemedTk

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self):
        if self.produtos:
            messagebox.showinfo("Estoque","Produto removido.")
            self.produtos.pop(0)
        else:
            messagebox.showerror("Estoque", "Produto não encontrado no estoque.")

    def exibir_estoque(self):
        return self.produtos

class FilaPedidos:
    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def processar_pedido(self):
        if self.pedidos:
            return self.pedidos.pop(0)
        else:
            messagebox.showerror("Erro", "Não há pedidos na fila.")
            return None

    def exibir_pedidos(self):
        return self.pedidos

class PilhaVendas:
    def __init__(self):
        self.vendas = []

    def push(self, venda):
       
            self.vendas.insert(0, venda)

    def pop(self):
        if self.vendas:
            return self.vendas.pop(0)
        else:
            messagebox.showerror("Erro", "A pilha de vendas está vazia.")
            return None

    def top(self):
        if self.vendas:
            return self.vendas[0]
        else:
            messagebox.showerror("Erro", "A pilha de vendas está vazia.")
            return None

    def size(self):
        return len(self.vendas)

    def empty(self):
        return len(self.vendas) == 0

    def registrar_venda(self, venda):
    
            self.push(venda)

    def desfazer_venda(self):
        if not self.empty():
            venda_desfeita = self.pop()
            return venda_desfeita
        else:
            messagebox.showerror("Erro", "Não há vendas registradas.")
            return None

    def exibir_vendas(self):
        return self.vendas
class InterfaceGrafica:
    def __init__(self, master):
        self.master = master
        self.master.resizable(False, False) 
        self.master.title("Controle de Estoque")

        self.estoque = Estoque()
        self.fila_pedidos = FilaPedidos()
        self.pilha_vendas = PilhaVendas()

        self.frame_estoque = tk.Frame(self.master, bg="#f0f0f0", pady=10)
        self.frame_estoque.pack(padx=10, pady=10, side=tk.LEFT)

        self.label_estoque = tk.Label(self.frame_estoque, text="Estoque:", font=("Arial", 12), bg="#f0f0f0")
        self.label_estoque.pack()

        self.text_estoque = tk.Text(self.frame_estoque, height=5, width=30, font=("Arial", 10))
        self.text_estoque.pack()

        self.btn_adicionar_produto = tk.Button(self.frame_estoque, text="Adicionar Produto", font=("Arial", 10), bg="teal", command=self.adicionar_produto)
        self.btn_adicionar_produto.pack(pady=5, side=tk.LEFT)

        self.btn_remover_produto = tk.Button(self.frame_estoque, text="Remover Produto", font=("Arial", 10), bg="#ce0018", command=self.remover_produto)
        self.btn_remover_produto.pack(pady=5, side=tk.LEFT)
        
        self.frame_pedidos = tk.Frame(self.master, bg="#f0f0f0", pady=10)
        self.frame_pedidos.pack(padx=10, pady=10, side=tk.LEFT)

        self.label_pedidos = tk.Label(self.frame_pedidos, text="Pedidos:", font=("Arial", 12), bg="#f0f0f0")
        self.label_pedidos.pack()

        self.text_pedidos = tk.Text(self.frame_pedidos, height=5, width=30, font=("Arial", 10))
        self.text_pedidos.pack()

        self.btn_adicionar_pedido = tk.Button(self.frame_pedidos, text="Adicionar Pedido", font=("Arial", 10), bg="teal", command=self.adicionar_pedido)
        self.btn_adicionar_pedido.pack(pady=5, side=tk.LEFT)

        self.btn_processar_pedido = tk.Button(self.frame_pedidos, text="Processar Pedido", font=("Arial", 10), bg="#ffff00", command=self.processar_pedido)
        self.btn_processar_pedido.pack(pady=5, side=tk.LEFT)

        
        self.frame_vendas = tk.Frame(self.master, bg="#f0f0f0", pady=10)
        self.frame_vendas.pack(padx=10, pady=10, side=tk.LEFT)

        self.label_vendas = tk.Label(self.frame_vendas, text="Vendas:", font=("Arial", 12), bg="#f0f0f0")
        self.label_vendas.pack()

        self.text_vendas = tk.Text(self.frame_vendas, height=5, width=30, font=("Arial", 10))
        self.text_vendas.pack()

        self.btn_registrar_venda = tk.Button(self.frame_vendas, text="Registrar Venda", font=("Arial", 10), bg="teal", command=self.registrar_venda)
        self.btn_registrar_venda.pack(pady=5, side=tk.LEFT)

        self.btn_desfazer_venda = tk.Button(self.frame_vendas, text="Desfazer Venda", font=("Arial", 10), bg="#ce0018", command=self.desfazer_venda)
        self.btn_desfazer_venda.pack(pady=5, side=tk.LEFT)


        self.atualizar_estoque()
        self.atualizar_pedidos()
        self.atualizar_vendas()

    def adicionar_produto(self):
        produto = simpledialog.askstring("Adicionar Produto", "Digite o nome do produto:")
        if produto:
            self.estoque.adicionar_produto(produto)
            self.atualizar_estoque()

    def remover_produto(self):
        self.estoque.remover_produto()
        self.atualizar_estoque()

    def adicionar_pedido(self):
        pedido = simpledialog.askstring("Adicionar Pedido", "Digite o nome do pedido:")
        if pedido:
            if pedido in self.estoque.exibir_estoque():
                self.fila_pedidos.adicionar_pedido(pedido)
                self.atualizar_pedidos()
            else:
                messagebox.showinfo("Esgotado!", "Nenhum produto no estoque!")

    def processar_pedido(self):
        pedido = self.fila_pedidos.processar_pedido()
        if pedido:
            if pedido in self.estoque.exibir_estoque():
                self.estoque.remover_produto()
                self.pilha_vendas.registrar_venda(pedido)
                self.atualizar_pedidos()
                self.atualizar_estoque()
                self.atualizar_vendas()
            else:
                messagebox.showerror("Erro", "Produto não encontrado no estoque!")
        else:
            messagebox.showerror("Erro", "Não há pedidos na fila")

    def registrar_venda(self):
        venda = simpledialog.askstring("Registrar Venda", "Digite o nome da venda:")
        if venda in self.estoque.exibir_estoque():
            self.pilha_vendas.registrar_venda(venda)
            self.estoque.remover_produto()
            self.atualizar_vendas()
            self.atualizar_estoque()
        else:
            messagebox.showerror("Erro", "Produto não encontrado no estoque!")

    def desfazer_venda(self):
        venda_desfeita = self.pilha_vendas.desfazer_venda()
        if venda_desfeita:
            self.estoque.adicionar_produto(venda_desfeita)
            self.atualizar_vendas()
            self.atualizar_estoque()

    def atualizar_estoque(self):
        self.text_estoque.delete(1.0, tk.END)
        estoque = self.estoque.exibir_estoque()
        for produto in estoque:
            self.text_estoque.insert(tk.END, produto + "\n")

    def atualizar_pedidos(self):
        self.text_pedidos.delete(1.0, tk.END)
        pedidos = self.fila_pedidos.exibir_pedidos()
        for pedido in pedidos:
            self.text_pedidos.insert(tk.END, pedido + "\n")

    def atualizar_vendas(self):
        self.text_vendas.delete(1.0, tk.END)
        vendas = self.pilha_vendas.exibir_vendas()
        for venda in vendas:
            self.text_vendas.insert(tk.END, venda + "\n")

if __name__ == "__main__":
    root = ThemedTk("black")
    interface = InterfaceGrafica(root)
    root.mainloop()
