def generate_pyi(output_file="MyGame.pyi"):
    from ServiceRegistry import ServiceRegistry
    import MyGame

    services = ServiceRegistry._services

    lines = []

    # -----------------------------
    # MyGame static methods
    # -----------------------------
    lines.append("class MyGame:")
    lines.append("    @staticmethod")
    lines.append("    def Construct(): ...")
    lines.append("")
    lines.append("    @staticmethod")
    lines.append("    def Initialize(): ...")
    lines.append("")
    lines.append("    @staticmethod")
    lines.append("    def LoadContent(): ...")
    lines.append("")
    lines.append("    @staticmethod")
    lines.append("    def Update(game_time: float): ...")
    lines.append("")
    lines.append("    @staticmethod")
    lines.append("    def Draw(): ...")
    lines.append("")

    # -----------------------------
    # Manager facade
    # -----------------------------
    lines.append("    class Manager:")
    lines.append("        ...")

    for name, instance in services.items():
        cls_name = instance.__class__.__name__
        lines.append(f"        {name}: {cls_name}")

    content = "\n".join(lines)

    with open(output_file, "w") as f:
        f.write(content)

    print(f"Generated {output_file}")


if __name__ == "__main__":
    from bootstrap import build_game

    build_game()
    generate_pyi()