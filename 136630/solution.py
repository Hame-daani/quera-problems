def sort_dependencies(packages, package_name):
    package_dependencies = []
    for pkg in packages[package_name]:
        package_dependencies.extend(sort_dependencies(packages, pkg))
    package_dependencies.extend(packages[package_name])
    return list(dict.fromkeys(package_dependencies))
