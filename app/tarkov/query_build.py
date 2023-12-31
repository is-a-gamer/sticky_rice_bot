import json

from pydantic.types import Dict, List


class GQueryBuilder(object):
    search_type: str = ""
    args: Dict = {}
    return_field = []

    def __init__(self, search_type: str, args: Dict, return_field: List):
        self.search_type = search_type
        self.args = args
        if "lang" not in args.keys():
            args["lang"] = "zh"
        if "limit" not in args.keys():
            args["limit"] = 10
        self.return_field = return_field

    def build(self):
        search_args = []
        for key in self.args.keys():
            if key == "name" or key == "ids":
                search_args.append(f'{key}: "{self.args[key]}"')
                continue
            search_args.append(f'{key}: {self.args[key]}')

        search_args_str = ", ".join(search_args)
        return_field_str = "\n    ".join(self.return_field)
        return json.dumps({"query": f'''
{{
  {self.search_type}({search_args_str}) {{
    {return_field_str}
  }}
}}
'''}, indent=4)


def item_base_query(args):
    return GQueryBuilder(search_type="items", args=args,
                         return_field=["id", "name", "shortName", "link", "basePrice", "iconLink",
                                       "lastLowPrice","avg24hPrice"]).build()


def item_price_query(args):
    return GQueryBuilder(search_type="items", args=args, return_field=["name",
                                                                       "basePrice",
                                                                       "lastLowPrice",
                                                                       "types",
                                                                       "updated",
                                                                       "iconLink",
                                                                       "avg24hPrice",
                                                                       "sellFor{price,currency,vendor{name,normalizedName}}"]).build()


def hideout_stations_query(args):
    return GQueryBuilder(search_type="hideoutStations", args=args, return_field=["name",
                                                                                 "levels{level,itemRequirements{item{name}count}}"]).build()
