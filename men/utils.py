from men.models import Category, Thing

menu = [{'title': 'Басты бет','url_name': 'home'},
        {'title': 'Біз туралы','url_name': 'about'},
        {'title': 'Мопед қосу','url_name': 'add_product'},
        {'title': 'Заттар', 'url_name': 'product'},
        {'title': 'Байланыс', 'url_name': 'contact'}

        ]
regis = [{'title':'Тіркелу','url_name':'registration'},
         {'title':'Кіру','url_name':'login'}
         ]

class DataMixin:
        def get_user_context(self,**kwargs):
                context=kwargs
                cats = Category.objects.all()

                user_menu = menu.copy()
                if not self.request.user.is_authenticated:
                        user_menu.pop(2)

                context['menu'] = user_menu
                context['cats']=cats
                context['regis'] = regis
                if 'cat_selected' not in context:
                        context['cat_selected']=0
                return context