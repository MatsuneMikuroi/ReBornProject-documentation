class DocumentInfos:

    title = u'Reborn Project'
    first_name = 'Romain'
    last_name = 'De Groote'
    author = f'{first_name} {last_name}'
    year = u'2022'
    month = u'Décembre'
    seminary_title = u'Travail personnel d\' OCI'
    tutor = u"Cédric Donner"
    release = "(Version intermédiaire)"
    repository_url = "https://github.com/donnerc/prog-dynamique"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()