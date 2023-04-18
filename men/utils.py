from men.models import Category, Thing

menu = [{'title': 'Басты бет','url_name': 'home'},
        {'title': 'Біз туралы','url_name': 'about'},
        {'title': 'Мопед қосу','url_name': 'add_product'},
        {'title': 'Қызметтер','url_name': 'qyzmet'},
        {'title': 'Заттар', 'url_name': 'product'},
        {'title': 'Байланыс', 'url_name': 'contact'}

        ]

class DataMixin:
        def get_user_context(self,**kwargs):
                context=kwargs
                cats = Category.objects.all()
                context['menu'] = menu
                context['cats']=cats
                # context['regis'] = regis
                if 'cat_selected' not in context:
                        context['cat_selected']=0
                return context