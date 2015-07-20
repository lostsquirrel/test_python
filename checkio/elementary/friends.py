# -*- coding:utf-8 -*-
__author__ = 'lisong'

"""
For the mission "How to find friends" , it’s nice to have access to a specially made data structure.
In this mission we will realize a data structure which we will use to store and work with a friend network.

The class "Friends" should contains names and the connections between them.
Names are represented as strings and are case sensitive.
Connections are undirected, so if "sophia" is connected with "nikola", then it's also correct in reverse.

class Friends(connections)

Returns a new Friends instance. "connections" is an iterable of sets with two elements in each.
Each connection contains two names as strings. Connections can be repeated in the initial data,
but inside it's stored once. Each connection has only two states - existing or not.

>>> Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
>>> Friends([{"1", "2"}, {"3", "1"}])

add(connection)

Add a connection in the instance. "connection" is a set of two names (strings).
Returns True if this connection is new. Returns False if this connection exists already.

>>> f = Friends([{"1", "2"}, {"3", "1"}])
>>> f.add({"1", "3"})
False
>>> f.add({"4", "5"})
True

remove(connection)

Remove a connection from the instance. "connection" is a set of two names (strings).
Returns True if this connection exists. Returns False if this connection is not in the instance.

>>> f = Friends([{"1", "2"}, {"3", "1"}])
>>> f.remove({"1", "3"})
True
>>> f.remove({"4", "5"})
False

names()

Returns a set of names. The set contains only names which are connected with somebody.

>>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"}))
>>> f.names()
{"a", "b", "c", "d"}
>>> f.remove({"d", "c"})
True
>>> f.names()
{"a", "b", "c"}

connected(name)

Returns a set of names which is connected with the given "name".
If "name" does not exist in the instance, then return an empty set.

>>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
>>> f.connected("a")
{"b", "c"}
>>> f.connected("d")
set()
>>> f.remove({"c", "a"})
True
>>> f.connected("c")
{"b"}
>>> f.remove({"c", "b"})
True
>>> f.connected("c")
set()

In this mission all data will be correct and you don't need to implement value checking.

Input: Statements and expression with the Friends class.

Output: The behaviour as described.

How it is used: Here you will implement a class with mutable states.
This is not a simple structure with a couple of functions, but object representation with more complex structure.

Precondition: All data is correct.
"""
class Friends:
    def __init__(self, connections):
        self.network = dict()
        for connection in connections:
            self.add(connection)

    def add(self, connection):
        def add_item(key, value):
            flag = True
            print key, value
            if key in self.network:
                names = self.network.get(key)

                print value, names
                if value in names:
                    flag = False
                else:
                    names.add(value)
            else:
                names = set()
                names.add(value)
                self.network[key] = names

            return flag

        name_a = connection.pop()
        name_b = connection.pop()
        # print name_a, name_b
        add_item(name_a, name_b)

        return add_item(name_b, name_a)

    def remove(self, connection):
        def remove_item(key, value):
            flag = False
            items = self.network.get(key)
            if items is not None:
                if value in items:
                    items.remove(value)
                    flag = True
                    if len(items) == 0:
                        self.network.pop(key)
            return flag

        name_a = connection.pop()

        name_b = connection.pop()

        remove_item(name_a, name_b)
        return remove_item(name_b, name_a)

    def names(self):

        names = self.network.keys()
        # print type(names), names
        return set(names)

    def connected(self, name):
        names = self.network.get(name)
        if names is None:
            names = set()

        return names



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    # print letter_friends.network
    # digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    # assert letter_friends.add({"c", "d"}) is True, "Add"
    # assert letter_friends.add({"c", "d"}) is False, "Add again"
    # assert letter_friends.remove({"c", "d"}) is True, "Remove"
    # assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    # # print letter_friends.network
    # # print letter_friends.names(), type(letter_friends.names())
    # assert letter_friends.names() == {"a", "b", "c"}, "Names"
    # assert letter_friends.connected("d") == set(), "Non connected name"
    # assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
    f = Friends([{"And", "Or"}, {"For", "And"}])
    print f.network
    print f.add({"Or", "And"})

'''
class Friends():
    def __init__(self, connections):
        self.all_connection = list(connections)
​
    def add(self, connection):
        if connection in self.all_connection:
            return False
        else:
            self.all_connection.append(connection)
            return True
​
    def remove(self, connection):
        if connection in self.all_connection:
            self.all_connection.remove(connection)
            return True
        else:
            return False
​
    def names(self):
        return reduce(lambda a,b: a.union(b), self.all_connection)

    def connected(self, name):
        related = [pair for pair in self.all_connection if name in pair]
        if related:
            related = reduce(lambda a,b: a.union(b), related)
            related.remove(name)
            return related
        else:
            return set([])
'''
