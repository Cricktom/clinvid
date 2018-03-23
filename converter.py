class JsonConverter(object):
    """docstring for JsonConverter."""
    def __init__(self, arg):
        self.to_parse = arg

    #split name and return name json
    def name_split(self, name):
        tokens = name.split('<')
        first=""
        middle=""
        last=""
        if(len(tokens)>=4):
            if (len(tokens[1])>1):
                first = tokens[1][:-1]
            if (len(tokens[2])>1):
                middle = tokens[2][:-1]
            if (len(tokens[3])>0):
                last = tokens[3][:-1]
        return {"first":first, "middle":middle,"last":last }

    #splits location and return location json

    def location_split(self, location):
        tokens = location.split("<")
        name = ""
        lng = ""
        lat = ""
        if(len(tokens)>=4):
            if(len(tokens[1])>1):
                name = tokens[1][:-1]
            if(len(tokens[3])>1):
                lng = tokens[3][:-1]
            if(len(tokens[4])>2):
                lat = tokens[4][:-1]
        return {"name":name,"coords":{"lat":lat,"long":lng}}

    #split followers and return follower json
    def follower_split(self, followers):
        tokens = followers.split("@@|")
        result=[]
        for follower in tokens:
            fl_token = follower.split("|")
            if(len(fl_token)>0):
                id = fl_token[0]
                name = self.name_split(fl_token[1])
                location = self.location_split(fl_token[2])
                img = fl_token[3]
                result.append({"id":id,"imageId":img, "name":name, "location":location})
        return result

    #parse the string into desired json
    def parse(self):
        str_tkn = self.to_parse.split('**')
        profile = str_tkn[0]
        followers = str_tkn[1]
        profile_token = profile.split('|')
        id = profile_token[1]
        name = self.name_split(profile_token[2])
        location = self.location_split(profile_token[3])
        img = profile_token[4]
        follower = self.follower_split(followers[10:])
        return {"id":id, "name":name,"location":location,"imageId":img, "followers":follower}
