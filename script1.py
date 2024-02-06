import pandas as pd
from connection import define_engine


def read_table(nombre_tabla):
    engine = define_engine()
    consulta_sql = f"SELECT * FROM {nombre_tabla}"
    df = pd.read_sql(consulta_sql, con=engine)
    engine.dispose()  
    return df

def calculate_central_tendency_stats(df, column):
    mean = df[column].mean()
    median = df[column].median()
    mode = df[column].mode().iloc[0]  
    return mean, median, mode

def read_sql(sql):
    engine = define_engine()
    df = pd.read_sql(sql, con=engine)
    engine.dispose()  
    return df


if __name__ == "__main__":

    # First question
    # nombre_tabla = "customer" 
    # df = read_table(nombre_tabla)
    # print(df)
    # print("\nEstadísticas de la tabla 'customer':")
    # print(df.describe())

    #Second question
    # df = read_table("payment", "amount")
    # print("\nOperaciones de Tendencia Central de la tabla 'payment':")
    # mean, median, mode = calculate_central_tendency_stats(df)
    # print(f"Media: {mean}")
    # print(f"Mediana: {median}")
    # print(f"Moda: {mode}")

    #Third question
    # df = read_table("film")
    # column = 'replacement_cost'
    # print("\nOperaciones de Tendencia Central de la tabla 'film' campo 'replacement_cost':")
    # mean, median, mode = calculate_central_tendency_stats(df, column)
    # print(f"Media: {mean}")
    # print(f"Mediana: {median}")
    # print(f"Moda: {mode}")

    #Fourth question
    sql = "select p.payment_id, p.amount, c.country from payment p " \
        "inner join customer cu on cu.customer_id = p.customer_id " \
        "inner join address a on cu.address_id = a.address_id " \
        "inner join city ci on ci.city_id = a.city_id " \
        "inner join country c on c.country_id = ci.country_id " \
        "where c.country = 'Peru';"
    df = read_sql(sql)
    column = 'amount'
    print("\nOperaciones de Tendencia Central de la tabla 'payment':")
    mean, median, mode = calculate_central_tendency_stats(df, )
    print(f"Media: {mean}")
    print(f"Mediana: {median}")
    print(f"Moda: {mode}")