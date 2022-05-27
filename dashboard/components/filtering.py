from dash import dcc
from data.external import tips_df


# tworzymy funkcje odpowiedzialna za stworzenie slidera
def tips_range_slider() -> dcc.RangeSlider:
    df = tips_df()  # ladowanie datasetu
    min_ = int(df.tip.min())
    max_ = int(df.tip.max())
    mean_ = int(df.tip.mean())
    std_ = int(df.tip.std())

    # tworzenie slaidera
    slider = dcc.RangeSlider(
        min=min_,
        max=max_,
        step=1,
        value=[mean_ - std_, mean_ + std_],
        id="tips-range-slider",
    )
    return slider
