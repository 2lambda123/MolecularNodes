from addon_helper import get_version
import MolecularNodes as mn

mn.pkg.install_package('pytest-snapshot')
import pytest

@pytest.fixture
def bpy_module(cache):
    return cache.get("bpy_module", None)

# ensure we can successfully install all of the required pacakges 
def test_install_packages(bpy_module):
    mn.pkg.install_all_packages()
    assert mn.pkg.is_current('biotite') == True

def test_versionID_pass(bpy_module):
    expect_version = (2, 6, 2)
    return_version = get_version(bpy_module)
    assert expect_version == return_version

def test_versionID_fail(bpy_module):
    expect_version = (2, 5, 0)
    return_version = get_version(bpy_module)
    assert not expect_version == return_version

# able to load a structure without any trouble
def test_load_rcsb(bpy_module):
    mol, file = mn.load.open_structure_rcsb('4ozs')
    assert 1 == 1

def test_node_surface(bpy_module):
    obj = mn.load.molecule_rcsb('6n2y')
    name = 'MOL_style_surface_split_6n2y'
    split_surface_node = mn.nodes.create_custom_surface(name, len(obj['chain_id_unique']))
    assert split_surface_node.name == name

def test_import_snapshot(snapshot):
    import pickle
    import io
    
    obj = mn.load.molecule_rcsb('4ozs')
    
    vertices_str = ""
    for v in obj.data.vertices:
        vertices_str += "{},{},{}\n".format(v.co.x, v.co.y, v.co.z)

    snapshot.assert_match(vertices_str, '4ozs_verts.txt')