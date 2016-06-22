class veiculo(object):
    def set_id(self, i):
        self.id = i

    def get_id(self):
        return int(self.id)

    def set_data(self, d):
        self.data = d

    def get_data(self):
        return str(self.data)

    def set_x(self, a):
        self.x = a

    def set_y(self, b):
        self.y = b

    def set_horario(self, h):
        self.horario = h

    def __str__(self):
        return str(self.id) + " " + str(self.data)+ "," + str(self.horario) + "," + \
               str(self.x) + "," + str(self.y)

    def __str1__(self):
        return " " + str(self.data) + "," + str(self.horario) + "," + \
            str(self.x) + "," + str(self.y)