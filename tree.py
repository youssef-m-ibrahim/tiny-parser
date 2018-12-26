from random import *
from random import *
from scanner import *
from graphviz import Graph
class Node:
    children = []
    def __init__(self, info):
        self.info = info
    def __delete__(self, instance):
        for child in self.children:
            del child


class Parser:
    global_pointer = int()
    scan = Scanner()
    counter = 0
    graph = Graph(comment='The Round Table')
    # Constructor
    def __init__(self):
        self.global_pointer = 0

    def returnAsNode(self, buffer = 0):
        return Node(self.scan.tokens[self.global_pointer + buffer][0])

    # Functions ( Procedures )  for the Grammar rules

    def match(self, token, option):
        # option da 7aeb2a 7agten bool y3ne 0 lw el token 7aqarnw bl value, 1 -> type
        # Example1 match( '(' , 0)
        # Example2 match( 'number' , 1)
        prev_pointer = self.global_pointer
        if(self.global_pointer<len(self.scan.tokens) and token == self.scan.tokens[self.global_pointer][option]):
            self.global_pointer += 1
            return True
        self.global_pointer = prev_pointer
        return False

    def factor(self):
        prev_pointer = self.global_pointer
        if (self.match('number',1)):
            return self.returnAsNode(-1)
        if (self.match('identifier', 1)):
            return self.returnAsNode(-1)
        # match '(' and exp and ')'
        if (self.match('(',0)):
            node = self.expression()
            if node is not None and self.match(')',0):
                return node
        self.global_pointer = prev_pointer
        return None

    def term(self):
        prev_pointer = self.global_pointer
        parent_node = self.factor()
        if(parent_node  is not None):
            current_node = None
            current_parent = None
            while (self.match('*', 0) or self.match('/', 0)  ):
                node_1 = self.returnAsNode(-1)
                right_node = self.factor()
                if(right_node is None):
                    self.global_pointer = prev_pointer
                    return None
                if current_node is None:
                    node_1.children = [parent_node, right_node]
                    parent_node = node_1
                else:
                    node_1.children = [current_parent.children[1], right_node]
                    current_parent.children[1] = node_1
                current_node = right_node
                current_parent = node_1
            return parent_node
        return None

    def simple_exp(self):
        prev_pointer = self.global_pointer
        parent_node = self.term()
        if (parent_node is not None):
            current_node = None
            current_parent = None
            while (self.match('+', 0) or self.match('-', 0)):
                node_1 = self.returnAsNode(-1)
                right_node = self.term()
                if (right_node is None):
                    self.global_pointer = prev_pointer
                    return None
                if current_node is None:
                    node_1.children = [parent_node, right_node]
                    parent_node = node_1
                else:
                    node_1.children = [current_parent.children[1], right_node]
                    current_parent.children[1] = node_1
                current_node = right_node
                current_parent = node_1
            return parent_node
        return None

    def expression(self):
        prev_pointer = self.global_pointer
        left_node = self.simple_exp()
        if left_node is not None and (self.match('<', 0) or self.match('=', 0)):
            parent_node = self.returnAsNode(-1)
            right_node = self.simple_exp()
            if right_node is not None:
                parent_node.children = [left_node, right_node]
                return parent_node
        self.global_pointer = prev_pointer
        node = self.simple_exp()
        if(node is not None):
            return node
        self.global_pointer = prev_pointer
        return None

    def if_statement(self):
        prev_pointer = self.global_pointer
        if self.match('if',0):
            parent_node = self.returnAsNode(-1)
            child_node_1 = self.expression()
            if child_node_1 is not None:
                if self.match('then',0):
                    child_node_2 = self.stmt_seq()
                    if child_node_2 is not None:
                        if self.match('end',0):
                            parent_node.children = [child_node_1, child_node_2]
                            return parent_node
        self.global_pointer = prev_pointer
        if self.match('if',0):
            parent_node = self.returnAsNode(-1)
            child_node_1 = self.expression()
            if child_node_1 is not None:
                if self.match('then',0):
                    child_node_2 = self.stmt_seq()
                    if child_node_2 is not None:
                        if self.match('else',0):
                            child_node_3 = self.stmt_seq()
                            if child_node_3 is not None:
                                if self.match('end', 0):
                                    parent_node.children = [child_node_1, child_node_2, child_node_3]
                                    return parent_node
        self.global_pointer = prev_pointer
        return None

    def repeat_statement(self):
        prev_pointer = self.global_pointer
        if self.match('repeat', 0):
            parent_node = self.returnAsNode(-1)
            left_node = self.stmt_seq()
            if left_node is not None:
                if self.match('until', 0):
                    right_node = self.expression()
                    if right_node is not None:
                        parent_node.children = [left_node, right_node]
                        return parent_node
        self.global_pointer = prev_pointer
        return None

    def assign_statement(self):
        prev_pointer = self.global_pointer
        if(self.match('identifier', 1)):
            left_node = self.returnAsNode(-1)
            if self.match(':=', 0):
                parent_node = self.returnAsNode(-1)
                right_node = self.expression()
                if right_node is not None:
                    parent_node.children = [left_node, right_node]
                    return parent_node
        self.global_pointer = prev_pointer
        return None

    def read_statement(self):
        prev_pointer = self.global_pointer
        if(self.match('read',0) and self.match('identifier',1)):
            node = self.returnAsNode(-2)
            node.children = [self.returnAsNode(-1)]
            return node
        self.global_pointer = prev_pointer
        return None

    def write_statement(self):
        prev_pointer = self.global_pointer
        if (self.match('write', 0) and self.expression()):
            node = self.returnAsNode(-2)
            node.children = [self.returnAsNode(-1)]
            return node
        self.global_pointer = prev_pointer
        return None

    def statement(self):
        prev_pointer = self.global_pointer
        node = self.if_statement()
        if(node is not None):
            return node
        self.global_pointer = prev_pointer
        node = self.repeat_statement()
        if (node is not None):
            return node
        self.global_pointer = prev_pointer
        node = self.write_statement()
        if (node is not None):
            return node
        self.global_pointer = prev_pointer
        node = self.read_statement()
        if (node is not None):
            return node
        self.global_pointer = prev_pointer
        node = self.assign_statement()
        if (node is not None):
            return node
        self.global_pointer = prev_pointer
        return None

    def stmt_seq(self):
        prev_pointer = self.global_pointer
        parent_node = self.statement()
        if(parent_node  is not None):
            flag = True
            while(self.match(';',0)):
                node = self.statement()
                if(node is None):
                    self.global_pointer = prev_pointer
                    return None
                if flag:
                    temp = Node('statements')
                    temp.children = [parent_node, node]
                    parent_node = temp
                    flag = False
                else:
                    parent_node.children.append(node)
            if self.global_pointer != len(self.scan.tokens):
                if (self.scan.tokens[self.global_pointer][0] == 'end'
                    or
                    self.scan.tokens[self.global_pointer][0] == 'else'
                    or
                    self.scan.tokens[self.global_pointer][0] == 'until'):
                    pass
                else:
                    return  None
            return parent_node
        return None

    def program(self):
        node = self.stmt_seq()
        if(node is not None):
            self.draw(node)
            print(self.graph.source)  # doctest: +NORMALIZE_WHITESPACE
            self.graph.render('test-output/round-table'+str(uniform(0,100))+'.gv', view=True)
            return True
        return False

    def draw(self, node):
        index = str(self.counter)
        self.graph.node(index, node.info)
        self.counter += 1
        for child in node.children:
            self.graph.edge(self.draw(child),index)
        return index




