
class CSVCreation:
    def __init__(self, layers):
        self.layers = layers

    def output_csv(self):
        f = open("log_csv.csv", "w")
        f.write("Layer,x,y\n")
        for layer in self.layers:
            for point in layer.points:
                f.write("%i, %d, %d\n" % (layer.layer_id, point.x, point.y))
        return "log_csv.csv"

                
