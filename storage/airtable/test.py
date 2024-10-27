from airtable import airtable

baseid="appEQUUwfybXiZZ8B" 
tablename="Table 1"
token="patpPk9MhH1Lcc11e.cdf0f8132b1df82090763ef160e4d795e56b605913fb9c4ae0629ff2c2656fa3"
at = airtable.Airtable(baseid,tablename,token)
# result = [(page) for page in con.get()]