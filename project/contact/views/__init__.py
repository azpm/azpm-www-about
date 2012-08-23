from .base import Index, ContactPerson, Thanks

__all__ = ['index','person','thanks']

index = Index.as_view()
person = ContactPerson.as_view()
thanks = Thanks.as_view()