import unittest
"""
E-mail:
    [a-Z][0-9]@[a-Z].[]
    Start-EMA-Domain-Ext
"""
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
"""
FILE PATH TEST:
def test(filepath->str)->str:
    #Validate{
            - Filepath -> Correct, Exists
            - Parse -> Json.load->open or throw exception
            - Check keys and Values
    # Read register _order_store_json || (load)->(gives and array with the objects) which is an orderid ->check it exists
        - Iterate through the file and break when the file found the orderid
            - If it doesnt exists -> exception
            - If exists & found -> break
            - Compute the hash "manually" and check if the hash is correct
            - If its correct, Create Order request object 


"""



if __name__ == '__main__':
    unittest.main()
