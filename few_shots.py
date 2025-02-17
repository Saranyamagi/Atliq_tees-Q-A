few_shots = [
    {'Question' : "How many t-shirts do we have left for Nike in XS size and white color?",
     'SQLQuery' : "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "91"},
    
    {'Question': "How much is the total price of the inventory for all S-size t-shirts?",
     'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE size = 'S'",
     'SQLResult': "Result of the SQL query",
     'Answer': "22292"},

    {'Question': "How much is the total price of the inventory for all XL-size t-shirts?",
     'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE size = 'XL'",
     'SQLResult': "Result of the SQL query",
     'Answer': "19580"},

    {'Question': "If we have to sell all the Levi’s T-shirts today with discounts applied, how much revenue will our store generate (post-discounts)?",
     'SQLQuery': """SELECT SUM(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) AS total_revenue 
                    FROM (SELECT SUM(price * stock_quantity) AS total_amount, t_shirt_id 
                          FROM t_shirts 
                          WHERE brand = 'Levi' 
                          GROUP BY t_shirt_id) a 
                    LEFT JOIN discounts ON a.t_shirt_id = discounts.t_shirt_id""",
     'SQLResult': "Result of the SQL query",
     'Answer': "16725.4"},

    {'Question' : "If we have to sell all the Levi’s T-shirts today, how much revenue will our store generate without discount?",
     'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "17462"},

    {'Question': "How many white color Levi's shirts do we have in stock?",
     'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "290"},

    {'Question': "How much sales revenue will be generated if we sell all large size t-shirts today in Nike brand after applying discounts?",
     'SQLQuery': """SELECT SUM(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) AS total_revenue 
                    FROM (SELECT SUM(price * stock_quantity) AS total_amount, t_shirt_id 
                          FROM t_shirts 
                          WHERE brand = 'Nike' AND size = 'L' 
                          GROUP BY t_shirt_id) a 
                    LEFT JOIN discounts ON a.t_shirt_id = discounts.t_shirt_id""",
     'SQLResult': "Result of the SQL query",
     'Answer' : "290"},

    {'Question': "What is the total inventory price of all the t-shirts that have the size of XL?",
     'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE size = 'XL';",
     'SQLResult': "Result of the SQL query",
     'Answer': "The total inventory price of all XL-sized t-shirts is $327."},

    {'Question': "What is the total inventory price of all the t-shirts that have the size of M and color red?",
     'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE size = 'M' AND color = 'red';",
     'SQLResult': "Result of the SQL query",
     'Answer': "The total inventory price of all M-sized red t-shirts is $180."},

    # Added new examples that explicitly address product price calculations
    {'Question': "What is the total revenue if we sell all the extra-large size t-shirts for Adidas at a discount rate of 20%?",
     'SQLQuery': """SELECT SUM(price * stock_quantity * (1 - 0.2)) AS total_revenue 
                    FROM t_shirts 
                    WHERE size = 'XL' AND brand = 'Adidas';""",
     'SQLResult': "Result of the SQL query",
     'Answer': "The total revenue from selling all XL-sized Adidas t-shirts at 20% discount is $2250."},

    {'Question': "How much inventory value does the store have for all red XL t-shirts from Nike?",
     'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND size = 'XL' AND color = 'red';",
     'SQLResult': "Result of the SQL query",
     'Answer': "The total inventory value of red XL Nike t-shirts is $3150."},
]
