# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import re

CHARACTER_LEVEL_DEFAULT = True
SPACE_NORMALIZER = re.compile(r"\s+")


def tokenize_line(line, character_level=CHARACTER_LEVEL_DEFAULT):
    line = SPACE_NORMALIZER.sub(" ", line)
    line = line.strip()
    return list(line) if character_level else line.split()
