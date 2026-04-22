import typer
from rich.console import Console
from rich.table import Table
from rich import print as rprint
from bot.orders import place_order
from bot.logging_config import setup_logger


# ── Initialize App ────────────────────────────────────
app = typer.Typer(
    help="Binance Futures Testnet Trading Bot"
)
console = Console()
logger = setup_logger("cli")


@app.command()
def trade(
    symbol: str = typer.Option(
        ...,
        help="Trading pair e.g. BTCUSDT"
    ),
    side: str = typer.Option(
        ...,
        help="BUY or SELL"
    ),
    order_type: str = typer.Option(
        ...,
        "--order-type",
        help="MARKET or LIMIT or STOP_MARKET"
    ),
    quantity: float = typer.Option(
        ...,
        help="Order quantity e.g. 0.001"
    ),
    price: float = typer.Option(
        None,
        help="Price — required for LIMIT orders only"
    ),
):
    """
    Place a futures order on Binance Futures Testnet.
    """

    # ── Print Request Summary ─────────────────────
    console.rule("[bold blue] Order Request Summary")
    rprint(f"  Symbol      : [cyan]{symbol.upper()}[/cyan]")
    rprint(f"  Side        : [green]{side.upper()}[/green]")
    rprint(f"  Order Type  : [yellow]{order_type.upper()}[/yellow]")
    rprint(f"  Quantity    : [white]{quantity}[/white]")
    if price:
        rprint(f"  Price       : [white]{price}[/white]")

    # ── Place Order ───────────────────────────────
    try:
        response = place_order(
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        # ── Print Success ─────────────────────────
        console.rule("[bold green] Order Placed Successfully ✅")

        # Build response table
        table = Table(
            show_header=True,
            header_style="bold magenta"
        )
        table.add_column("Field",  style="cyan",  width=20)
        table.add_column("Value",  style="white", width=30)

        # Fields to show from Binance response
        fields = [
            "orderId",
            "symbol",
            "status",
            "side",
            "type",
            "origQty",
            "executedQty",
            "avgPrice",
            "updateTime"
        ]

        for field in fields:
            if field in response:
                table.add_row(field, str(response[field]))

        console.print(table)
        logger.info(
            f"Order placed successfully. "
            f"OrderId: {response.get('orderId')}"
        )

    # ── Handle Validation Errors ──────────────────
    except ValueError as ve:
        console.rule("[bold red] Validation Error ❌")
        rprint(f"[red]{ve}[/red]")
        logger.warning(f"Validation error: {ve}")
        raise typer.Exit(code=1)

    # ── Handle All Other Errors ───────────────────
    except Exception as e:
        console.rule("[bold red] Order Failed ❌")
        rprint(f"[red]Error: {e}[/red]")
        logger.exception("Order placement failed.")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()