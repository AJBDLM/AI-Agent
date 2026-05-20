import plotly.express as px


class ChartAgent:

    def generate_chart(self, df):

        cols = df.columns.tolist()

        if len(cols) < 2:
            return None

        x = cols[0]
        y = cols[1]

        fig = px.bar(df, x=x, y=y)

        return fig
