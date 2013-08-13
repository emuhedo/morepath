import morepath
    
app = morepath.App()

@app.root()
class Root(object):
    pass

class Model(object):
    def __init__(self, id):
        self.id = id

@app.model(model=Model, path='{id}',
           variables=lambda model: { 'id': model.id })
def get_model(id):
    return Model(id)

@app.resource(model=Model)
def default(request, model):
    return "The resource for model: %s" % model.id

@app.resource(model=Model, name='link')
def link(request, model):
    return request.link(model)

@app.resource(model=Root)
def root_default(request, model):
    return "The root"

@app.resource(model=Root, name='link')
def root_link(request, model):
    return request.link(model)
