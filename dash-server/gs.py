import dash_html_components as html

goldman_sachs_page = html.Div([
    html.Div([  # subpage 1

        # Row 1 (Header)

        html.Div([

            html.Div([
                html.H5(
                    'Goldman Sachs Strategic Absolute Return Bond II Portfolio'),
                html.H6('A sub-fund of Goldman Sachs Funds, SICAV',
                        style={'color': '#7F90AC'}),
            ], className="nine columns padded"),

            html.Div([
                html.H1(
                    [html.Span('03', style={'opacity': '0.5'}), html.Span('17')]),
                html.H6('Monthly Fund Update')
            ], className="three columns gs-header gs-accent-header padded", style={'float': 'right'}),

        ], className="row gs-header gs-text-header"),

        html.Br([]),

        # Row 2

        html.Div([

            html.Div([
                html.H6('Investor Profile',
                        className="gs-header gs-text-header padded"),

                html.Strong('Investor objective'),
                html.P('Capital appreciation and income.',
                       className='blue-text'),

                html.Strong(
                    'Position in your overall investment portfolio*'),
                html.P('The fund can complement your portfolio.',
                       className='blue-text'),

                html.Strong('The fund is designed for:'),
                html.P('The fund is designed for investors who are looking for a flexible \
                        global investment and sub-investment grade fixed income portfolio \
                        that has the ability to alter its exposure with an emphasis on interest \
                        rates, currencies and credit markets and that seeks to generate returns \
                        through different market conditions with a riskier investment strategy \
                        than GS Strategic Absolute Return Bond I Portfolio.', className='blue-text'),

            ], className="four columns"),
        ], className="row "),
    ], className="subpage"),
], className="page")