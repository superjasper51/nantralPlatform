import { adaptTranslatedField } from '#shared/infra/translatedFields/translatedField.adapter';

import { Shortcut } from '../shortcut.type';
import { ShortcutDTO } from './shortcut.dto';

export function adaptShortcut(shortcutDTO: ShortcutDTO): Shortcut {
  return {
    title: shortcutDTO.title,
    titleTranslated: adaptTranslatedField(shortcutDTO, 'title'),
    description: shortcutDTO.description,
    descriptionTranslated: adaptTranslatedField(shortcutDTO, 'description'),
    icon: shortcutDTO.icon,
    link: shortcutDTO.link,
  };
}
