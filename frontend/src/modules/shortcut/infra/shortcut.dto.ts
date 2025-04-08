import { TranslatedFieldsDTO } from '#shared/infra/translatedFields/translatedField.dto';

export type ShortcutDTO = {
  title: string;
  description: string;
  icon: string;
  link: string;
} & TranslatedFieldsDTO<'title' | 'description'>;
