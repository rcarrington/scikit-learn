import numpy


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('sparsetools', parent_package, top_path)

    config.add_extension('_min_spanning_tree',
                         sources=['_min_spanning_tree.c'],
                         include_dirs=[numpy.get_include()],
                         #libraries=libraries
                         )
    config.add_extension('_traversal',
                         sources=['_traversal.c'],
                         include_dirs=[numpy.get_include()],
                         #libraries=libraries
                         )
    config.add_extension('_graph_tools',
                         sources=['_graph_tools.c'],
                         include_dirs=[numpy.get_include()],
                         #libraries=libraries
                         )

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
