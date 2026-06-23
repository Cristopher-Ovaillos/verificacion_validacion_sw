def before_scenario(context, scenario):
    from src.gestor_flota import GestorFlota
    GestorFlota._reset_para_tests()
