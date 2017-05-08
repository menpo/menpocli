from os.path import isfile
from pathlib import Path

import menpo.io as mio
from menpo.io.input.base import importer_for_filepath, image_types


def build_landmark_output_path(img_path, i=0):
    name = img_path.stem + ('_' + str(i) if i > 0 else '')
    return img_path.parent / '{}.pts'.format(name)


def can_import_img(path):
    try:
        importer_for_filepath(path, image_types)
        return True
    except ValueError:
        return False


def resolve_all_paths(img_paths_or_patterns):
    img_paths = set()
    for img_path_or_pattern in img_paths_or_patterns:
        if not isfile(img_path_or_pattern):
            img_paths.update(set(mio.image_paths(img_path_or_pattern)))
        else:
            img_paths.add(Path(img_path_or_pattern))
    return img_paths


def resolve_importable_paths(img_paths_or_patterns):
    img_paths = resolve_all_paths(img_paths_or_patterns)
    importable_img_paths = set(filter(can_import_img, img_paths))
    non_importable = img_paths - importable_img_paths

    if len(non_importable) > 0:
        missing_str = '\n    ' + '\n    '.join([str(p)
                                                for p in non_importable])
        print('Warning: {} files provided are not '
              'importable by menpo:{}'.format(len(non_importable),
                                              missing_str))
    print('Found {} images that will be '
          'processed.'.format(len(importable_img_paths)))
    return img_paths


def save_pointcloud_as_landmark(img_path, i, pointcloud):
    mio.export_landmark_file(pointcloud,
                             build_landmark_output_path(img_path),
                             overwrite=True)
