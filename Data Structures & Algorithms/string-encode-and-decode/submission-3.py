class Solution:
    '''
    


    '''




    def encode(self, strs: List[str]) -> str:
        encode_dict = dict(enumerate(strs))
        return str(encode_dict)

    def decode(self, s: str) -> List[str]:
        decode_dict = eval(s)
        decode_list = list(decode_dict.values())
        return decode_list