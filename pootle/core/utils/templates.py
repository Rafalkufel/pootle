#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from django.conf import settings
from django.template.base import TemplateDoesNotExist
from django.template.loader import find_template_loader


def get_template_source(name, dirs=None):
    """Retrieves the template's source contents.

    :param name: Template's filename, as passed to the template loader.
    :param dirs: list of directories to optionally override the defaults.
    :return: tuple including file contents and file path.
    """
    loaders = []
    for loader_name in settings.TEMPLATE_LOADERS:
        loader = find_template_loader(loader_name)
        if loader is not None:
            # The cached loader includes the actual loaders underneath
            if hasattr(loader, 'loaders'):
                loaders.extend(loader.loaders)
            else:
                loaders.append(loader)

    for loader in loaders:
        try:
            return loader.load_template_source(name, template_dirs=dirs)
        except TemplateDoesNotExist:
            pass

    raise TemplateDoesNotExist(name)
