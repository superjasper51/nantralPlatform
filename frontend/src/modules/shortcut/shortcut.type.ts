import { TranslatedFieldObject } from '#shared/infra/translatedFields/translatedField.types';

export interface Shortcut {
  title: string;
  titleTranslated: TranslatedFieldObject;
  description: string;
  descriptionTranslated: TranslatedFieldObject;
  icon: string;
  link: string;
}
