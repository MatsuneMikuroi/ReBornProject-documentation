class DocumentInfos:

    title = u'Reborn Project'
    first_name = 'Romain'
    last_name = 'De Groote'
    author = f'{first_name} {last_name}'
    year = u'2023'
    month = u'Février'
    seminary_title = u'Travail personnel d\' OCI'
    tutor = u"Cédric Donner"
    release = "Version finale"
    repository_url = "https://github.com/MatsuneMikuroi/ReBornProject"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

infos = DocumentInfos()